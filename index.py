# 1
def update_profile(user_id, **kwargs):
    return {
        'id': user_id, 
        'updated_fields': kwargs
        }
# 2
def get_domains(emails):
    return (email.split('@')[1] for email in emails)

# 3
def filter_target_audience(users):
    return (user for user in users if user['age'] >= 18 and user ['is_premium'])

# 4
def build_response(status_code, *errors, **payload):
    return {
        'status': status_code,
        'errors': errors,
        'data': payload
    }

# 5
def calculate_total_spent(transactions):
    return sum(transactions['amount'] for transactions in transactions)