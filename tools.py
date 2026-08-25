
from pyscript import document, when
import math
import re
import statistics

def current_lang():
    return document.documentElement.lang or "tr"

def tr_en(tr, en):
    return tr if current_lang().startswith("tr") else en

def parse_numbers(text):
    parts = re.split(r"[\s,;]+", text.strip())
    values = []
    for part in parts:
        if part:
            values.append(float(part))
    return values

def metric(label_tr, label_en, value):
    label = tr_en(label_tr, label_en)
    return f'<div class="metric"><span>{label}</span><strong>{value}</strong></div>'

@when("click", "#calculate")
def calculate(event=None):
    raw = document.querySelector("#data-input").value
    output = document.querySelector("#result")
    try:
        values = parse_numbers(raw)
        if len(values) < 2:
            output.innerHTML = tr_en(
                "En az iki sayısal gözlem girin.",
                "Enter at least two numeric observations."
            )
            return

        n = len(values)
        mean = statistics.fmean(values)
        median = statistics.median(values)
        stdev = statistics.stdev(values)
        minimum = min(values)
        maximum = max(values)
        cv = (stdev / mean * 100) if mean != 0 else math.nan
        cv_text = tr_en("Tanımsız", "Undefined") if math.isnan(cv) else f"%{cv:.2f}"

        output.innerHTML = (
            '<div class="result-grid">'
            + metric("n", "n", str(n))
            + metric("Ortalama", "Mean", f"{mean:.3f}")
            + metric("Medyan", "Median", f"{median:.3f}")
            + metric("Std. sapma", "Std. deviation", f"{stdev:.3f}")
            + metric("Minimum", "Minimum", f"{minimum:.3f}")
            + metric("Maksimum", "Maximum", f"{maximum:.3f}")
            + metric("Aralık", "Range", f"{maximum - minimum:.3f}")
            + metric("Değişim katsayısı", "Coefficient of variation", cv_text)
            + "</div>"
        )
    except ValueError:
        output.innerHTML = tr_en(
            "Girdiyi kontrol edin. Yalnızca sayısal değerler kullanın; ondalık ayırıcı olarak nokta kullanın.",
            "Check the input. Use numeric values only and a period as the decimal separator."
        )

@when("click", "#example")
def load_example(event=None):
    document.querySelector("#data-input").value = "12, 15, 18, 18, 21, 22, 24, 27"
    calculate()

@when("click", "#clear")
def clear_all(event=None):
    document.querySelector("#data-input").value = ""
    document.querySelector("#result").innerHTML = tr_en(
        "Sonuçlar burada görünecek.",
        "Results will appear here."
    )
