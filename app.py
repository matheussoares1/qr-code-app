
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import qrcode
import io
import re

app = Flask(__name__)
app.secret_key = "change-me"  # necessário para flash messages

URL_REGEX = re.compile(
    r'^(https?://)'  # http:// ou https://
    r'([\w.-]+)'     # domínio
    r'([:/?#][^\s]*)?$',
    re.IGNORECASE
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        link = (request.form.get("link") or "").strip()

        if not URL_REGEX.match(link):
            flash("Informe uma URL válida, incluindo http:// ou https://")
            return redirect(url_for("index"))

        # Criar QR Code em memória
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(link)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Salvar em memória
        buf = io.BytesIO()
        img.save(buf, "PNG")
        buf.seek(0)

        return send_file(buf, mimetype="image/png", as_attachment=True, download_name="qrcode.png")

    return render_template("index.html")

if __name__ == "__main__":
    # Tornar acessível fora do container
    app.run(host="0.0.0.0", port=5000, debug=False)
