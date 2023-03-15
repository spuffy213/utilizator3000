import opentele.api
import pyrogram
import pyrogram.errors
import asyncio
import rich.console

def get_clietn(
    phone
):
    api = opentele.api.API.TelegramIOS.Generate()
    return pyrogram.client.Client(
        name = phone,
        api_id = 1,
        api_hash = 'b6b154c3707471f5339bd661645ed3d6',
        app_version = api.app_version,
        device_model = api.device_model,
        system_version = api.system_version,
    )


async def main():
    c = rich.console.Console()
    phone = '+79512069910'
    while True:
        try:
            client = get_clietn(phone)
            async with client:
                sent_code = await client.send_code(
                    phone_number = phone
                )
                await asyncio.sleep(1)
                await client.resend_code(
                    phone_number = phone,
                    phone_code_hash = sent_code.phone_code_hash
                )
        except pyrogram.errors.FloodWait as exception:
            time_to_wait = exception.value
            c.log(f'waiting {time_to_wait} seconds')
            await asyncio.sleep(int(time_to_wait)) # type: ignore
        except Exception:
            c.print_exception()

asyncio.run(
    main()
)

