# -*- coding: utf-8 -*-
import asyncio
import json
import sys
from urllib.parse import urlparse


async def tcp_echo_client(loop, h, p):
    reader, writer = await asyncio.open_connection(h, p, loop=loop)
    while True:
        data = await reader.readline()
        received = json.loads(data.decode().strip())

        print(f'in\t{received}')

        type = received['type']

        if type == 'hello':
            response = {
                'type': 'join',
                'name': 'tsumogiri',
                'room': None
            }
        elif type == 'start_game':
            id = received['id']
            response = {'type': 'none'}
        elif type == 'end_game':
            break
        elif type == 'tsumo':
            if received['actor'] == id:
                response = {
                    'type': 'dahai',
                    'actor': id,
                    'pai': received['pai'],
                    'tsumogiri': True,
                }
            else:
                response = {'type': 'none'}
        elif type == 'error':
            break
        else:
            response = {'type': 'none'}

        send_string = json.dumps(response, separators=(',', ':')) + '\n'
        print(f'out\t{send_string}')

        writer.write(send_string.encode())
        await writer.drain()


if __name__ == '__main__':
    parsed = urlparse(sys.argv[1])
    host, port = parsed.netloc.split(':')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client(loop, host, int(port)))
    loop.close()
