def num_unique_emails(emails: list[str]):
    valid_email_set = set()
    for email in emails:
        local_name = email.split("@")[0]
        domain = email.split("@")[-1]
        local_name = local_name.split("+")[0]
        local_name = local_name.replace(".", "")
        email = local_name + "@" + domain
        valid_email_set.add(email)
    print(valid_email_set)
    return len(valid_email_set)


print(num_unique_emails(['a@leetcode.com', 'b@leetcode.com', "c@leetcode.com"]))
print(num_unique_emails(['test.email+alex@leetcode.com',
                         'test.e.mail+bob.cathy@leetcode.com',
                         'testemail+david@lee.tcode.com',
                         ]))

