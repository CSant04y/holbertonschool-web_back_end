# 0x01. Python - Async
# Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/T060wv57F2YSq0Xj6AO9iA) , **without the help of Google**:

### async and await syntax
```
async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r
```
### How to execute an async program with asyncio
```
if __name__ == "__main__":
    random.seed(444)
'''You run the program by calling the main'''
    r1, r2, r3 = asyncio.run(main())
    print()
    print(f"r1: {r1}, r2: {r2}, r3: {r3}")

```
