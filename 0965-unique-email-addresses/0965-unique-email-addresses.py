class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse_email(email):
            split_emails = email.split("@")
            email = []

            for char in split_emails[0]:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    email.append(char)
            return "".join(email) + "@" + split_emails[1]

        counts = Counter()
        for email in emails:
            email_addr = parse_email(email) 
            print(email_addr)
            counts[email_addr] += 1
        
        return len(counts)
