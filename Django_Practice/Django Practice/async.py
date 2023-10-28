import asyncio

# tasks 

# async def waiter()-> None:
#     task1=asyncio.create_task(cook('pasta',8))
#     task2=asyncio.create_task(cook('Caeser Salad',3))
#     task3=asyncio.create_task(cook('Lamb Chops',16))
#     await task1; await task2; await task3

# async def cook(order:str,time_to_prepare:int)->None:
#     print(f'Getting {order}, order')
#     await asyncio.sleep(time_to_prepare)
#     print(order, 'ready')
# asyncio.run(waiter())


# co-routine

async def waiter()-> None:
    await (cook('pasta',8))
    await (cook('Caeser Salad',3))
    await (cook('Lamb Chops',16))


async def cook(order:str,time_to_prepare:int)->None:
    print(f'Getting {order}, order')
    await asyncio.sleep(time_to_prepare)
    print(order, 'ready')
asyncio.run(waiter())

