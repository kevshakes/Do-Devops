import boto3

# Step 1: Create a DynamoDB table
def create_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    table.wait_until_exists()
    print(f"Table '{table_name}' created successfully.")


# Step 2: Add items to the table
def add_item(table_name, item_data):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=item_data)
    print(f"Item added successfully: {response}")


# Step 3: Query the table and Remove an item
def query_and_remove_item(table_name, item_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Query the table to check if the item exists
    response = table.query(
        KeyConditionExpression='id = :val',
        ExpressionAttributeValues={
            ':val': item_id
        }
    )

    if response['Items']:
        # Remove the item if it exists
        response = table.delete_item(
            Key={
                'id': item_id
            }
        )
        print(f"Item with ID {item_id} removed successfully: {response}")
    else:
        print(f"Item with ID {item_id} not found in the table.")


# Step 4: Delete the table
def delete_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    table.delete()
    table.wait_until_not_exists()
    print(f"Table '{table_name}' deleted successfully.")


if __name__ == "__main__":
    # Step 1: Get the table name from the user
    table_name = input("Enter the DynamoDB table name: ")
    create_table(table_name)

    # Step 2: Get the table item data from the user
    item_id = input("Enter the item ID (integer) to add to the table: ")
    item_name = input("Enter the item name: ")
    item_age = input("Enter the item age: ")

    item_data = {
        'id': int(item_id),
        'name': item_name,
        'age': int(item_age)
    }
    add_item(table_name, item_data)

    # Step 3: Get the item ID to remove from the user
    item_id_to_remove = input("Enter the item ID (integer) to remove from the table: ")
    query_and_remove_item(table_name, int(item_id_to_remove))

    # Step 4: Delete the table
    delete_table(table_name)
