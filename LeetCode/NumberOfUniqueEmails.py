def numUniqueEmails(emails):
    def validateEmail(email):

        try:
            indexOfAt = email.index('@')
            localName = email[: indexOfAt]
            after = email[indexOfAt:]
            localName = localName.replace('.', '')
            try:
                localName = localName[:localName.index('+')]
            except ValueError:
                print("No plus found")
            return localName+after
        except ValueError:
            print('Missing at sign')
            return

    nameSet = set()
    for email in emails:
        nameSet.add(validateEmail(email))
    print(len(nameSet))
    return len(nameSet)


# cleaner solution from somebody else
def numUniqueEmails(self, emails) -> int:
    # addresses will be stored here
    distinct_emails = []
    for mail in emails:                                 # for every single mail
        # split local and domain part
        splitted = mail.split('@')
        # remove dots from the local part
        splitted[0] = splitted[0].replace('.', '')

        # find "+", -1 is returned when there isn't any "+"
        idx = splitted[0].find('+')
        if idx != -1:
            # cut "+" and everything afterward for local part
            splitted[0] = splitted[0][:idx]

        # full_email = '@'.join(splitted)               # unnecessary step as we care only about amount

        if splitted not in distinct_emails:             # add to the list only if there isn't the same email
            distinct_emails.append(splitted)

    return len(distinct_emails)


numUniqueEmails(
    ['robhen010@gmail.com', 'rob.henderson@gmail.com', 'rob.r.henderson@gmail.com'])

numUniqueEmails(["test.email+alex@leetcode.com",
                 "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"])
