class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for domain in cpdomains:
            parameters = domain.split(" ")
            count = int(parameters[0])
            domains = parameters[1]
            left = 0
            right = len(domains)
            while left < right:
                subdomain = domains[left:right]
                if subdomain in counts:
                    counts[subdomain] = counts[subdomain] + count
                else:
                    counts[subdomain] = count
                while left < len(domains) and domains[left] != '.':
                    left += 1
                left += 1 # to skip '.'
        res = []
        for domain in counts:
            s = str(counts[domain]) + " " + domain
            res.append(s)
        return res
            
            
