import java.util.*;

class numUniqueEmails{
	public static void main(String args[]){
		String emails[] = {"test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"};
		System.out.println(NumUniqueEmails(emails));
	}

	public static int NumUniqueEmails(String[] emails) {
        Set<String> normalized = new HashSet<String>();
        for (String email : emails) {
            String[] parts = email.split("@"); // split into local and domain parts.
            String[] local = parts[0].split("\\+"); // split local by '+'.
            normalized.add(local[0].replace(".", "") + "@" + parts[1]); // remove all '.', and concatenate '@' and domain.        
        }
        return normalized.size();
    }
}