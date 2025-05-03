class Solution:
    def is_valid_ipv4(self, ip):
        parts = ip.split('.')
        
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            
            if num < 0 or num > 255:
                return False
            
            if part != str(num):
                return False
        
        return True

    def is_valid_ipv6(self, ip):
        parts = ip.split(':')
        
        if len(parts) != 8:
            return False
        
        for part in parts:
            if len(part) < 1 or len(part) > 4:
                return False
            
            for char in part:
                if not (char.isdigit() or ('a' <= char.lower() <= 'f')):
                    return False
        
        return True

    def validIPAddress(self, queryIP):
        if self.is_valid_ipv4(queryIP):
            return "IPv4"
        
        elif self.is_valid_ipv6(queryIP):
            return "IPv6"
        
        else:
            return "Neither"
