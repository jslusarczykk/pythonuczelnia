total_tasks = 100  
completed_tasks = 65  

def check_test_passing(total_tasks, completed_tasks):
    passing_score = total_tasks * 0.5  
    if completed_tasks >= passing_score:
        print("Test passed!")
        print("Total tasks:", total_tasks)
        print("Correctly completed tasks:", completed_tasks)
    else:
        print("Test not passed. More work needed!")

check_test_passing(total_tasks, completed_tasks)