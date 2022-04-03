/*
 * @lc app=leetcode id=1 lang=c
 *
 * [1] Two Sum
 */

// @lc code=start


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#define PRIME 263
struct node {
    int val;
    struct node *next;
};
void inithashtable(struct node *);
void freehashtable(struct node *);


int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *result = (int *)malloc(sizeof(int)*2);
    struct node *hashtable = (struct node *)malloc(sizeof(struct node)*PRIME);
    if (result == NULL)
    {
        printf("Not enough memony");
        return NULL;
    }
    
    if (hashtable == NULL)
    {
        printf("Not enough memony");
        return NULL;
    }

    inithashtable(hashtable);

    for (int i = 0; i < numsSize; i++)
    {
        int hash_value = abs(nums[i]%PRIME);
        if (hashtable[hash_value].val = -1)
        {
            hashtable[hash_value].val = i;
        }
        else
        {
            struct node *new_node = (struct node *)malloc(sizeof(struct node));
            if (new_node == NULL)
            {
                printf("Not enough memony");
                return NULL;
            }
            new_node->val = i;
            new_node->next = hashtable[hash_value].next;
            hashtable[hash_value].next = new_node;
        }
    }

    for (int i = 0; i < numsSize; i++) 
    {
        int hash_value_to_find = abs(nums[i]%PRIME);
        if (hashtable[hash_value_to_find].val == -1)
        {
            continue;
        }
        else {
            if (nums[hashtable[hash_value_to_find].val] == target - nums[i] && hashtable[hash_value_to_find].val != i)
            {
                result[0] = i;
                result[1] = hashtable[hash_value_to_find].val;
                freehashtable(hashtable);
                return result;
            }
            else
            {
                struct node *temp = hashtable[hash_value_to_find].next;
                while (temp != NULL)
                {
                    if(nums[temp->val] == target-nums[i])
                    {
					    result[0] = i;
					    result[1] = temp->val;
				    	freehashtable(hashtable);
				    	return result;
				    }
			    	else
                    {
                        temp = temp->next;
                    }
                }
                
            }
        }
    }
    freehashtable(hashtable);
    return NULL;

}

void inithashtable(struct node *hashtable)
{
    for (int i = 0; i < PRIME; i++) {
        hashtable[i].val = -1;
        hashtable[i].next = NULL;

    }
};

void freehashtable(struct node *hashtable) 
{
    int i;
	for(i=0;i<PRIME;i++)
	{
		struct node* current = hashtable[i].next;
		while(current != NULL)
		{
			struct node* prev = current;
			current = current->next;
			free(prev);
			
		}
		free(current);
	}
};

// @lc code=end

