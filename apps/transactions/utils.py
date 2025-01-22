from apps.transactions.models import Transaction
from apps.accounts.models import Account


def update_user_balance_and_create_transaction_history(transaction_type_user_select: str,
                                                       amount_user_entered: int, account_number: str) -> bool:
    user_information = Account.object.filter(account_number=account_number)
    process_success_flag = False

    if transaction_type_user_select == "Withdrawal" and amount_user_entered <= user_information.balance:
        user_information.balance -= amount_user_entered
        process_success_flag = True

    elif transaction_type_user_select == "Deposit":
        user_information.balance += amount_user_entered
        process_success_flag = True

    else:
        return process_success_flag

    Transaction.objects.create(
        account=user_information,
        amount=amount_user_entered,
        transaction_type=transaction_type_user_select,
    )

    user_information.save()
    return process_success_flag
