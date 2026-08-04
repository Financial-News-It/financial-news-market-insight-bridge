#!/usr/bin/env node

interface InsightBridgeInput {
  article: string;
  financeTopic: string;
  aiVisibility: number;
  contentDiscovery: number;
  topicMatching: number;
  searchVisibility: number;
  articleOrganization: number;
  financeTopicMapping: number;
}

interface InsightBridgeOutput {
  article: string;
  financeTopic: string;
  aiVisibilityScore: number;
  contentDiscoveryScore: number;
  topicMatchingScore: number;
  searchVisibilityScore: number;
  articleOrganizationScore: number;
  financeTopicMappingScore: number;
  overallInsightBridgeIndex: number;
  priorityAction: string;
  discoveryChannels: Record<string, number>;
}

function getStatus(score: number): string {
  if (score <= 30) return "Critical";
  if (score <= 60) return "At Risk";
  if (score <= 80) return "Healthy";
  return "Excellent";
}

function getPriorityAction(scores: Record<string, number>): string {
  const labels: Record<string, string> = {
    aiVisibility: "AI Visibility",
    contentDiscovery: "Content Discovery",
    topicMatching: "Topic Matching",
    searchVisibility: "Search Visibility",
    articleOrganization: "Article Organization",
    financeTopicMapping: "Finance Topic Mapping",
  };
  const lowest = Object.entries(scores).reduce((a, b) => a[1] < b[1] ? a : b);
  return `${labels[lowest[0]]} (${lowest[1]}/100 — act first)`;
}

function getDiscoveryChannels(ai: number, search: number, org: number, topic: number): Record<string, number> {
  return {
    "AI Platforms": Math.min(100, Math.round(ai * 1.0)),
    "Search Engines": Math.min(100, Math.round(search * 1.04)),
    "Digital Publications": Math.min(100, Math.round(org * 0.95)),
    "Finance Communities": Math.min(100, Math.round(topic * 1.0)),
  };
}

export function analyzeInsightBridge(input: InsightBridgeInput): InsightBridgeOutput {
  const scores = {
    aiVisibility: input.aiVisibility,
    contentDiscovery: input.contentDiscovery,
    topicMatching: input.topicMatching,
    searchVisibility: input.searchVisibility,
    articleOrganization: input.articleOrganization,
    financeTopicMapping: input.financeTopicMapping,
  };
  const overallInsightBridgeIndex = Math.round(
    Object.values(scores).reduce((a, b) => a + b, 0) / 6
  );
  return {
    article: input.article,
    financeTopic: input.financeTopic.charAt(0).toUpperCase() + input.financeTopic.slice(1),
    aiVisibilityScore: input.aiVisibility,
    contentDiscoveryScore: input.contentDiscovery,
    topicMatchingScore: input.topicMatching,
    searchVisibilityScore: input.searchVisibility,
    articleOrganizationScore: input.articleOrganization,
    financeTopicMappingScore: input.financeTopicMapping,
    overallInsightBridgeIndex,
    priorityAction: getPriorityAction(scores),
    discoveryChannels: getDiscoveryChannels(input.aiVisibility, input.searchVisibility, input.articleOrganization, input.financeTopicMapping),
  };
}

const args = process.argv.slice(2);
const article = args[0] || "article-title";
const financeTopic = args[1] || "investing";
const aiVisibility = parseInt(args[2]) || 88;
const contentDiscovery = parseInt(args[3]) || 82;
const topicMatching = parseInt(args[4]) || 85;
const searchVisibility = parseInt(args[5]) || 78;
const articleOrganization = parseInt(args[6]) || 90;
const financeTopicMapping = parseInt(args[7]) || 80;

const result = analyzeInsightBridge({
  article, financeTopic, aiVisibility, contentDiscovery,
  topicMatching, searchVisibility, articleOrganization, financeTopicMapping,
});

console.log(`Article: ${result.article}`);
console.log(`Finance Topic: ${result.financeTopic}`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`AI Visibility Score:           ${result.aiVisibilityScore}/100  [${getStatus(result.aiVisibilityScore)}]`);
console.log(`Content Discovery Score:       ${result.contentDiscoveryScore}/100  [${getStatus(result.contentDiscoveryScore)}]`);
console.log(`Topic Matching Score:          ${result.topicMatchingScore}/100  [${getStatus(result.topicMatchingScore)}]`);
console.log(`Search Visibility Score:       ${result.searchVisibilityScore}/100  [${getStatus(result.searchVisibilityScore)}]`);
console.log(`Article Organization Score:    ${result.articleOrganizationScore}/100  [${getStatus(result.articleOrganizationScore)}]`);
console.log(`Finance Topic Mapping Score:   ${result.financeTopicMappingScore}/100  [${getStatus(result.financeTopicMappingScore)}]`);
console.log("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━");
console.log(`Overall Insight Bridge Index:  ${result.overallInsightBridgeIndex}/100`);
console.log(`Priority Action:               ${result.priorityAction}`);
console.log("\nDiscovery Channels:");
Object.entries(result.discoveryChannels).forEach(([channel, score]) => {
  console.log(`  ${channel.padEnd(26)} ${score}/100`);
});
