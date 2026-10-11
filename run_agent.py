#!/usr/bin/env python3
"""
Autonomous Research & Knowledge Agent
Main entry point for running research from the command line.
"""

import argparse
import sys
from rich.console import Console
from rich.markdown import Markdown
from core.crew import run_full_research
from memory.vector_store import ResearchMemory
from core.config import OPENAI_API_KEY

console = Console()


def check_setup():
    """Verify basic requirements before running."""
    if not OPENAI_API_KEY:
        console.print("[bold red]ERROR:[/bold red] OPENAI_API_KEY not found.")
        console.print("Please create a .env file with your OpenAI API key.")
        console.print("Example: OPENAI_API_KEY=sk-...")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Autonomous Research & Knowledge Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_agent.py "Impact of AI on software engineering"
  python run_agent.py "Quantum computing breakthroughs 2025" --depth deep
  python run_agent.py --list
  python run_agent.py --stats
        """
    )
    
    parser.add_argument(
        "topic",
        nargs="?",
        help="Research topic"
    )
    parser.add_argument(
        "--depth",
        choices=["quick", "standard", "deep"],
        default="standard",
        help="Research depth (default: standard)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all previously researched topics"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show memory statistics"
    )
    
    args = parser.parse_args()
    
    check_setup()
    
    # Handle utility commands
    if args.list or args.stats:
        memory = ResearchMemory()
        stats = memory.get_stats()
        
        if args.stats:
            console.print(f"\n[bold]Memory Statistics[/bold]")
            console.print(f"Total researches stored: {stats['total_researches']}")
        
        if args.list or args.stats:
            topics = stats["topics"]
            if topics:
                console.print(f"\n[bold]Researched Topics ({len(topics)}):[/bold]")
                for t in topics:
                    console.print(f"  • {t}")
            else:
                console.print("\n[dim]No previous research found.[/dim]")
        return
    
    # Require topic for research
    if not args.topic:
        # Interactive mode
        console.print("\n[bold cyan]Autonomous Research Agent[/bold cyan]")
        console.print("Enter a research topic (or 'q' to quit):\n")
        topic = console.input("[green]Topic → [/green]").strip()
        if not topic or topic.lower() in ("q", "quit", "exit"):
            console.print("Goodbye!")
            return
    else:
        topic = args.topic
    
    # Run research
    result = run_full_research(topic=topic, depth=args.depth)
    
    # Display the report
    console.print("\n" + "="*70)
    console.print(Markdown(result["report"]))
    console.print("="*70 + "\n")


if __name__ == "__main__":
    main()
