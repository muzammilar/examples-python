import xmpl

from box import Box

def main():
    config = Box(
        {
            "host":'clickhost',
            "port":8123,
            "username":'default',
            "password":''
        }
    )
    client = xmpl.ClickHouseClient(config)
    xmpl.setup_table(client)
    xmpl.query_data(client)


if __name__ == "__main__":
    main()
