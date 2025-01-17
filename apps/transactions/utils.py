from apps.transactions.models import Transaction
from apps.accounts.models import Account


def get_create_transaction_context(account_number_from_query, amount_user_entered, transaction_type_user_select):
    user_information = Account.objects.filter(account_number=account_number_from_query).first()

    process_transaction_flag = False

    if transaction_type_user_select == "Withdrawal" and amount_user_entered <= user_information.balance:
        user_information.balance -= amount_user_entered
        process_transaction_flag = True

    if transaction_type_user_select == "Deposit":
        user_information.balance += amount_user_entered
        process_transaction_flag = True

    if process_transaction_flag:

        Transaction.objects.create(
            account=user_information,
            amount=amount_user_entered,
            transaction_type=transaction_type_user_select,
        )

        user_information.save()
        context = {"message": f"Transaction Successful Your Current Balance is {user_information.balance}"}

        return context

    else:

        context = {"message": "Please enter the correct amount"}
        return context
