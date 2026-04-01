class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set() # emailusername [@] domain
        for email in emails:
            # parse
            email = email.split("@")
            local = email[0]
            local = local.replace('.', '')
            local = local.split("+")
            local = local[0]

            full_email = local + email[1]
            email_set.add(full_email)
        return len(email_set)