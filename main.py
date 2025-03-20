import os
import logging
import webbrowser
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Check if the ANTHROPIC_API_KEY is loaded from the environment
if not os.getenv("ANTHROPIC_API_KEY"):
    logging.warning("ANTHROPIC_API_KEY is not set. Falling back to browser-based search.")

    def browser_search(query):
        """Perform a search using the default web browser and display the search URL."""
        search_url = f"https://www.google.com/search?q={query}"
        logging.info(f"Opening browser for search: {search_url}")
        webbrowser.open(search_url)
        print(f"Search initiated. Please check your browser for results: {search_url}")
    
        # Modify the result using a tool (e.g., summarization or text processing)
        modified_result = f"Modified result for query: {query}"
        print(f"Modified Result: {modified_result}")

    def wikipedia_search(query):
        """Perform a search on Wikipedia and display the search URL."""
        wiki_url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        logging.info(f"Opening Wikipedia for search: {wiki_url}")
        webbrowser.open(wiki_url)
        print(f"Search initiated. Please check your browser for results: {wiki_url}")
        
        # Modify the result using a tool (e.g., summarization or text processing)
        modified_result = f"Modified result for query: {query}"
        print(f"Modified Result: {modified_result}")

    def gemini_search(query):
        """Perform a search using Gemini and display the search URL."""
        search_url = f"https://www.google.com/search?q=Gemini+{query}"
        logging.info(f"Opening browser for Gemini search: {search_url}")
        webbrowser.open(search_url)
        print(f"Search initiated. Please check your browser for results: {search_url}")
        
        # Modify the result using a tool (e.g., summarization or text processing)
        modified_result = f"Modified result for Gemini query: {query}"
        print(f"Modified Result: {modified_result}")

    def copilot_search(query):
        """Perform a search using Microsoft Copilot (simulated) and display the result."""
        logging.info(f"Performing Microsoft Copilot search for query: {query}")
        # Simulate a Microsoft Copilot search result
        copilot_result = f"Simulated Microsoft Copilot result for query: {query}"
        print(f"Microsoft Copilot Result: {copilot_result}")

    # Main loop for user interaction
    while True:
        try:
            query = input("What can I help you research? (Type 'exit' to quit): ").strip()
            if query.lower() == "exit":
                logging.info("Exiting the program. Goodbye!")
                break
            if not query:
                logging.warning("Query cannot be empty. Please try again.")
                continue

            # Ask the user which fallback search to use
            choice = input("Choose search method - (1) Google, (2) Wikipedia, (3) Gemini, (4) Copilot: ").strip()
            if choice == "1":
                browser_search(query)
            elif choice == "2":
                wikipedia_search(query)
            elif choice == "3":
                gemini_search(query)
            elif choice == "4":
                copilot_search(query)
            else:
                logging.warning("Invalid choice. Please select 1, 2, 3, or 4.")

        except Exception as e:
            logging.error("An error occurred: %s", e)
            retry = input("An error occurred. Would you like to try again? (yes/no): ").strip().lower()
            if retry != "yes":
                logging.info("Exiting the program. Goodbye!")
                break
