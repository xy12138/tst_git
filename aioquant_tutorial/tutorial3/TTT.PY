from aioquant import quant


def first_market():
    print('second tutorial')


if __name__ == "__main__":
    config_file = "/bolaipin/aioquant_zx/aioclass/tutorial3/config.json"
    quant.start(config_file, first_market)