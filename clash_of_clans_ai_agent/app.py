from agents.clash_agent import analyseClashOfClanData
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = sys.argv[1:]
    asyncio.run(analyseClashOfClanData(prompt=prompt))
    