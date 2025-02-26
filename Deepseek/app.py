from praisonaiagents import Agent

config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "praison",
            "path": ".praison"
        }
    },

    "llm": {
        "provider": "ollama",
        "config": {
            "model": "deepseek-r1:latest",
            "temperature": 0,
            "max_tokens": 8000,
            "ollama_base_url": "http://localhost:11434"
        }

    },

    "embedder": {
        "provider": "ollama",
        "config": {
            "model": "nomic-embed-text:latest",
            "ollama_base_url": "http://localhost:11434",
            "embedding_dims": 1536
        }
    }
}


try:
    agent = Agent(
        name="Knowledge Agent",
        instructions="You answers questions based on provided knowledge",
        knowledge=["KAG-Research-paper.pdf"],
        knowledge_config=config,
        user_id="user1",
        llm="deepseek-r1"
    )
    agent.start("Generate python code for random numbers")
except Exception as e:
    import traceback
    print(f"An error occurred: {e}")
    traceback.print_exc()

agent.start("Generate python code for random numbers")