from neo4j import GraphDatabase
import os

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "your_password_here")  # You can override with .env

class Neo4jConnector:
    def __init__(self, uri=NEO4J_URI, user=NEO4J_USER, password=NEO4J_PASSWORD):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters or {})

# Example usage
if __name__ == "__main__":
    db = Neo4jConnector()
    result = db.run_query("RETURN 'Neo4j connection successful' AS message")
    print([r["message"] for r in result])
    db.close()
