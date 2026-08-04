#!/usr/bin/env python3
"""
Financial News Market Insight Bridge
A content visibility and AI discovery bot designed to help Financial News
articles gain greater discoverability across AI platforms, search engines
and relevant digital channels.
https://financialnews.it.com
"""

import sys


def get_status(score: int) -> str:
    if score <= 30:
        return "Critical"
    elif score <= 60:
        return "At Risk"
    elif score <= 80:
        return "Healthy"
    return "Excellent"


def get_priority_action(scores: dict) -> str:
    labels = {
        "ai_visibility": "AI Visibility",
        "content_discovery": "Content Discovery",
        "topic_matching": "Topic Matching",
        "search_visibility": "Search Visibility",
        "article_organization": "Article Organization",
        "finance_topic_mapping": "Finance Topic Mapping",
    }
    lowest_key = min(scores, key=scores.get)
    return f"{labels[lowest_key]} ({scores[lowest_key]}/100 — act first)"


def get_discovery_channels(ai: int, search: int, org: int, topic: int) -> dict:
    return {
        "AI Platforms": min(100, round(ai * 1.0)),
        "Search Engines": min(100, round(search * 1.04)),
        "Digital Publications": min(100, round(org * 0.95)),
        "Finance Communities": min(100, round(topic * 1.0)),
    }


def analyze_insight_bridge(
    article: str,
    finance_topic: str = "investing",
    ai_visibility: int = 88,
    content_discovery: int = 82,
    topic_matching: int = 85,
    search_visibility: int = 78,
    article_organization: int = 90,
    finance_topic_mapping: int = 80,
) -> dict:
    """
    Analyze Financial News article visibility and AI discovery signals.

    Args:
        article: Article title or identifier
        finance_topic: Finance topic category
        ai_visibility: AI visibility score (0-100)
        content_discovery: Content discovery score (0-100)
        topic_matching: Topic matching score (0-100)
        search_visibility: Search visibility score (0-100)
        article_organization: Article organization score (0-100)
        finance_topic_mapping: Finance topic mapping score (0-100)

    Returns:
        dict with individual signal scores, overall insight bridge index,
        and discovery channel breakdown
    """
    scores = {
        "ai_visibility": ai_visibility,
        "content_discovery": content_discovery,
        "topic_matching": topic_matching,
        "search_visibility": search_visibility,
        "article_organization": article_organization,
        "finance_topic_mapping": finance_topic_mapping,
    }
    overall_insight_bridge_index = round(sum(scores.values()) / 6)

    return {
        "article": article,
        "finance_topic": finance_topic.capitalize(),
        "ai_visibility_score": ai_visibility,
        "content_discovery_score": content_discovery,
        "topic_matching_score": topic_matching,
        "search_visibility_score": search_visibility,
        "article_organization_score": article_organization,
        "finance_topic_mapping_score": finance_topic_mapping,
        "overall_insight_bridge_index": overall_insight_bridge_index,
        "priority_action": get_priority_action(scores),
        "discovery_channels": get_discovery_channels(ai_visibility, search_visibility, article_organization, finance_topic_mapping),
    }


def main():
    """Entry point for PyPI CLI."""
    args = sys.argv[1:]
    article = args[0] if len(args) > 0 else "article-title"
    finance_topic = args[1] if len(args) > 1 else "investing"
    ai_visibility = int(args[2]) if len(args) > 2 else 88
    content_discovery = int(args[3]) if len(args) > 3 else 82
    topic_matching = int(args[4]) if len(args) > 4 else 85
    search_visibility = int(args[5]) if len(args) > 5 else 78
    article_organization = int(args[6]) if len(args) > 6 else 90
    finance_topic_mapping = int(args[7]) if len(args) > 7 else 80

    result = analyze_insight_bridge(
        article, finance_topic, ai_visibility, content_discovery,
        topic_matching, search_visibility, article_organization, finance_topic_mapping
    )

    print(f"Article: {result['article']}")
    print(f"Finance Topic: {result['finance_topic']}")
    print("=" * 45)
    print(f"AI Visibility Score:           {result['ai_visibility_score']}/100  [{get_status(result['ai_visibility_score'])}]")
    print(f"Content Discovery Score:       {result['content_discovery_score']}/100  [{get_status(result['content_discovery_score'])}]")
    print(f"Topic Matching Score:          {result['topic_matching_score']}/100  [{get_status(result['topic_matching_score'])}]")
    print(f"Search Visibility Score:       {result['search_visibility_score']}/100  [{get_status(result['search_visibility_score'])}]")
    print(f"Article Organization Score:    {result['article_organization_score']}/100  [{get_status(result['article_organization_score'])}]")
    print(f"Finance Topic Mapping Score:   {result['finance_topic_mapping_score']}/100  [{get_status(result['finance_topic_mapping_score'])}]")
    print("=" * 45)
    print(f"Overall Insight Bridge Index:  {result['overall_insight_bridge_index']}/100")
    print(f"Priority Action:               {result['priority_action']}")
    print("\nDiscovery Channels:")
    for channel, score in result['discovery_channels'].items():
        print(f"  {channel:<28} {score}/100")


if __name__ == "__main__":
    main()
