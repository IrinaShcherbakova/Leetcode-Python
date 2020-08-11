class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return (1 if citations[0] > 0 else 0)
        citations.sort()
        total_papers = len(citations)
        h = 0
        
        for i in range(len(citations)-1, -1, -1):
            current_h = citations[i]
            papers_with_h_citations = total_papers - i
            if papers_with_h_citations >= current_h:
                return max(current_h, h)
            h = max(h, papers_with_h_citations)
             
        return h
