from parser import AvitoParser


def main(ap):
    ap.make_query()


if __name__ == "__main__":
    ap = AvitoParser(
        url="https://www.avito.ru/respublika_krym/zemelnye_uchastki/prodam-ASgBAgICAUSWA9oQ"
    )
    main(ap)
