import click
import uuid
import qrcode

from blabel import LabelWriter


@click.command()
@click.option('--count', default = 10)
@click.option('--target', default = "qrcodes.pdf")
def main(count, target):
    records = []
    for i in range(count):
        records.append(dict(uuid=str(uuid.uuid4()), error_correction = qrcode.constants.ERROR_CORRECT_H))

    print(records)

    label_writer = LabelWriter("item_template.html", default_stylesheets=("style.css",))
    label_writer.write_labels(records, target=target)

if __name__ == '__main__':
    main()
