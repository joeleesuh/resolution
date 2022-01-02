"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
 

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.

Solution
Overview
We need to clean the emails given to us. The most intuitive solution will be to iterate over the emails and clean them one by one.
Here, cleaning the email means removing unnecessary characters, per the rules given to us. Once an email has been cleaned, it can be pushed into a hash set. The size of this hash set will then equal the count of unique emails.


Rules to clean email:

If there are periods '.' in local name ignore them.
If there is a plus '+' in local name skip all local name characters till '@'.
There is only one '@' symbol and the substring after it is our domain name; we will keep the domain name as it is.
Approach 1: Linear Iteration
Intuition

We can iterate over an email from left to right, and add characters to local name until a '+' occurs, then we can skip all characters until '@' occurs, then we can again start appending the characters till the end of the email string to form the domain name.

Notice that per the rules, we do not need to read any characters between the first '+' and '@'. While checking each character from left to right, after finding the first '+' in the local name we can directly find the domain name by switching to a reverse iteration as there is only one '@' and we will skip all characters in between '+' and '@'.

This reduces the number of characters iterated, but the overall order time complexity remains the same.

For example, consider email = ab.c+abcdefghijklmnopqrstuvwxyz@leetcode.com.
Performing a linear scan from left to right, we will traverse all the characters in the given email.
Using the method proposed above, we can skip the characters from index 5 to index 30, thus saving time. However, keep in mind that because we read the domain name from right to left, we must also reverse the domain name before appending it to the local name. Thus, this improvement will be less effective when the domain name is long compared to the number of characters skipped.

Algorithm

For each email present in the emails array:
Iterate over the characters in the email and append each character to the local name if it is not '.'.
If the character is '+', do not append the character and break out of the loop.
Find the domain name using reverse traversal in the given email and append it to the string formed till now.
After cleaning the email insert it into the hash set.
Return the size of the hash set.
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Hash set to store all the unique emails.
        uniqueEmails = set()

        # Iterate over each character in email.
        for email in emails:
            cleanMail = []

            # Iterate over each character in email.
            for currChar in email:
                # Stop adding characters to localName.
                if currChar == '+' or currChar == '@':
                    break

                # Add this character if not '.'.
                if currChar != '.':
                    cleanMail.append(currChar)

            # Compute domain name (substring from end to '@').
            domainName = []
            for currChar in reversed(email):
                domainName.append(currChar)
                if currChar == '@':
                    break

            # Reverse domain name and append to local name.
            domainName = ''.join(domainName[::-1])
            cleanMail = ''.join(cleanMail)
            uniqueEmails.add(cleanMail + domainName)

        return len(uniqueEmails)

