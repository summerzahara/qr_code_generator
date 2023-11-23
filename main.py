import segno


def generate_qr(link, file_name):
    qr = segno.make_qr(link)
    qr.save(file_name, scale=5)


if __name__ == '__main__':
    generate_qr("http://www.google.com", "google_qr.png")
