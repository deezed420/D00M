import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

async def handle_client(client_reader, client_writer):
    client_address = client_writer.get_extra_info('peername')[0]
    logging.info("CONNECT - %s", client_address)

    try:
        while True:
            data = await client_reader.read(1024)
            if not data: break
            logging.info("RECEIVE - %s - %s", client_address, data.decode())
    except Exception as e:
        logging.error("Error in client handling: %s", e)
    finally:
        client_writer.close()
        logging.info("DETACH  - %s", client_address)

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 42069)
    logging.info("SERVER LISTENING")

    try:
        async with server:
            await server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Received KeyboardInterrupt. Closing the server.")
        server.close()
        await server.wait_closed()

if __name__ == "__main__": asyncio.run(main())