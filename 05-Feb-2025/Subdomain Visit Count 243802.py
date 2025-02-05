# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        split_domian = []
        parsed_domain = []
        expanded_domain =[]
        domain_dict = {}
        for i in range(len(cpdomains)):  
            split_domian.append(cpdomains[i].split('.'))  


        for i in range(len(split_domian)):
            temp = split_domian[i][0].split(" ")
            parsed_domain.append(temp + split_domian[i][1:])
            for j in range(len(split_domian[i])):
                if j < len(split_domian[i]):
                    expanded_domain.append(parsed_domain[i][0] +" "+ ".".join(parsed_domain[i][j+1:]))  
                    
        for i in expanded_domain:
            count , domain = i.split(" ")
            count = int(count)
            
            if domain in domain_dict:
                domain_dict[domain] += count
            else:
                domain_dict[domain] = count

        return [f"{count} {domain}" for domain,count in domain_dict.items()]