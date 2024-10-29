import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():

    tasks = [asyncio.create_task(start_strongman("Alex", 2)),
             asyncio.create_task(start_strongman("Max", 1.5)),
             asyncio.create_task(start_strongman("Apollon",5))]
    await asyncio.gather(*tasks)

asyncio.run(start_tournament())
