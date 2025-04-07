from server import server
import asyncio

def main():
    """Main entry point for the package."""
    asyncio.run(server.run())


if __name__ == "__main__":
    main()
