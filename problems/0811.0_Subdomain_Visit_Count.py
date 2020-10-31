'''
Success
Details 
Runtime: 40 ms, faster than 84.34% of Python online submissions for Subdomain Visit Count.
Memory Usage: 13.8 MB, less than 51.57% of Python online submissions for Subdomain Visit Count.
'''


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        subdomain = defaultdict(int)
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            domains = domain.split('.')
            subdomain[domain] += count
            
            if 2 == len(domains):
                subdomain[domains[1]] += count

            elif 3 == len(domains):
                subdomain[domains[2]] += count
                subdomain[domains[1] + '.' + domains[2]] += count
                
        visited = []
        for sub, count in subdomain.iteritems():
            visited.append('%s %s' % (str(count), sub))
        
        return visited
        