"""Gera auditoria diária verificável da base sintética de vendas.

O relatório documenta a execução dos controles, não uma melhoria diária no código.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "data" / "vendas.csv"
REPORT_DIR = ROOT / "reports" / "daily"
REQUIRED = {
    "pedido_id", "data", "cliente_id", "produto", "categoria",
    "quantidade", "preco_unitario", "cidade", "estado", "forma_pagamento",
}


def audit(path: Path) -> dict:
    """Calcula métricas e controles diretamente sobre o CSV versionado."""
    content_hash = hashlib.sha256(path.read_bytes()).hexdigest()
    with path.open("r", encoding="utf-8-sig", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        columns = set(reader.fieldnames or [])
        rows = list(reader)

    missing_columns = sorted(REQUIRED - columns)
    blank_cells = 0
    bad_quantities = 0
    bad_prices = 0
    bad_dates = 0
    total_items = 0
    total_revenue = Decimal("0.00")
    order_ids = set()
    seen_rows = set()
    duplicates = 0
    duplicated_orders = 0

    for row in rows:
        row_tuple = tuple((name, row.get(name)) for name in sorted(columns))
        if row_tuple in seen_rows:
            duplicates += 1
        seen_rows.add(row_tuple)

        blank_cells += sum(value is None or not str(value).strip() for value in row.values())
        order_id = (row.get("pedido_id") or "").strip()
        if order_id:
            if order_id in order_ids:
                duplicated_orders += 1
            order_ids.add(order_id)

        try:
            quantity = int(row.get("quantidade") or "")
            if quantity <= 0:
                raise ValueError
        except (ValueError, TypeError):
            bad_quantities += 1
            quantity = None

        try:
            price = Decimal(row.get("preco_unitario") or "")
            if not price.is_finite() or price <= 0:
                raise InvalidOperation
        except (InvalidOperation, ValueError, TypeError):
            bad_prices += 1
            price = None

        try:
            date.fromisoformat(row.get("data") or "")
        except ValueError:
            bad_dates += 1

        if quantity is not None and price is not None:
            total_items += quantity
            total_revenue += quantity * price

    quality = {
        "colunas_obrigatorias_ausentes": missing_columns,
        "celulas_vazias": blank_cells,
        "linhas_duplicadas": duplicates,
        "pedidos_duplicados": duplicated_orders,
        "quantidades_invalidas": bad_quantities,
        "precos_invalidos": bad_prices,
        "datas_invalidas": bad_dates,
    }
    passed = not any(quality.values()) and len(rows) > 0
    return {
        "sha256_base": content_hash,
        "status_qualidade": "aprovado" if passed else "atencao",
        "metricas": {
            "registros": len(rows),
            "pedidos_distintos": len(order_ids),
            "itens_validos_somados": total_items,
            "faturamento_simulado_valido_brl": str(total_revenue.quantize(Decimal("0.01"))),
        },
        "verificacoes": quality,
    }


def create_report(day: str) -> Path:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    earlier_reports = sorted(p for p in REPORT_DIR.glob("????-??-??.json") if p.stem < day)
    previous_hash = None
    if earlier_reports:
        previous = json.loads(earlier_reports[-1].read_text(encoding="utf-8"))
        previous_hash = previous.get("sha256_base")

    results = audit(CSV_PATH)
    changed = None if previous_hash is None else results["sha256_base"] != previous_hash
    report = {
        "data_verificacao_brasilia": day,
        "origem": "data/vendas.csv (base sintética, para estudo)",
        **results,
        "base_mudou_desde_relatorio_anterior": changed,
        "nota": (
            "Auditoria diária automatizada; novo relatório não significa novo desenvolvimento. "
            "As métricas descrevem apenas dados sintéticos versionados."
        ),
    }
    destination = REPORT_DIR / f"{day}.json"
    new_text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if destination.exists() and destination.read_text(encoding="utf-8") == new_text:
        print(f"Auditoria sem mudanças para {day}: nenhum novo commit necessário.")
    else:
        destination.write_text(new_text, encoding="utf-8")
        print(f"Auditoria registrada em {destination.relative_to(ROOT)}")
    print(f"Status da qualidade: {results['status_qualidade']}")
    print(f"Registros: {results['metricas']['registros']}")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description="Executa auditoria diária do CSV de vendas")
    parser.add_argument("--date", help="Data de referência YYYY-MM-DD para testes/reexecuções")
    args = parser.parse_args()
    day = (
        date.fromisoformat(args.date).isoformat()
        if args.date
        else datetime.now(ZoneInfo("America/Sao_Paulo")).date().isoformat()
    )
    create_report(day)


if __name__ == "__main__":
    main()
