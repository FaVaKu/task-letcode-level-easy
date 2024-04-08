class Solution(object):
    def countStudents(self, students, sandwiches):
        # Count wish
        preference_count = [0, 0]  # [0] for sandwiches[0], [1] for sandwiches[1]
        for student in students:
            preference_count[student] += 1
        
        # Iterate 
        for sandwich in sandwiches:
            if preference_count[sandwich] > 0:
                preference_count[sandwich] -= 1  # Reduce count for the chosen sandwich
            else:
                #stop
                break
        else:
            # If all students are served, return 0 (no students left unserved)
            return 0
        
        # Return the count of remaining unserved students
        return sum(preference_count)
