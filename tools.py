from pyscript import document, when
import math
import re
import statistics

def parse_numbers(text):
    parts = re.split(r"[\s,;]+", text.strip())
    values = []
    for part in parts:
        if part:
            values.append(float(part))
    return values

def metric(label, value):
    return f'<div class="metric"><span>{label}</span><strong>{value}</strong></div>'

@when("click", "#calculate")
def calculate(event=None):
    raw = document.querySelector("#data-input").value
    output = document.querySelector("#result")

    try:
        values = parse_numbers(raw)
        if len(values) < 2:
            output.innerHTML = "En az iki sayısal gözlem girin."
            return

        n = len(values)
        mean = statistics.fmean(values)
        median = statistics.median(values)
        stdev = statistics.stdev(values)
        minimum = min(values)
        maximum = max(values)
        cv = (stdev / mean * 100) if mean != 0 else math.nan
        cv_text = "Tanımsız" if math.isnan(cv) else f"%{cv:.2f}"

        output.innerHTML = (
            '<div class="result-grid">'
            + metric("n", str(n))
            + metric("Ortalama", f"{mean:.3f}")
            + metric("Medyan", f"{median:.3f}")
            + metric("Std. sapma", f"{stdev:.3f}")
            + metric("Minimum", f"{minimum:.3f}")
            + metric("Maksimum", f"{maximum:.3f}")
            + metric("Aralık", f"{maximum - minimum:.3f}")
            + metric("Değişim katsayısı", cv_text)
            + "</div>"
        )
    except ValueError:
        output.innerHTML = (
            "Girdiyi kontrol edin. Yalnızca sayısal değerler kullanın; "
            "ondalık ayırıcı olarak nokta kullanın."
        )

@when("click", "#example")
def load_example(event=None):
    document.querySelector("#data-input").value = "12, 15, 18, 18, 21, 22, 24, 27"
    calculate()

@when("click", "#clear")
def clear_all(event=None):
    document.querySelector("#data-input").value = ""
    document.querySelector("#result").innerHTML = "Sonuçlar burada görünecek."
