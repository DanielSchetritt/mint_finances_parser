CREATE TRIGGER duplicate_elimination
  after insert
  on finances
  begin
delete   from finances
where    transaction_id not in
         (
         select  min(transaction_id)
         from    finances
         group by
            finances.date
           ,finances.description
           ,finances.original_description
           ,finances.amount
           ,finances.transaction_type
           ,finances.account_name
           ,finances.labels
           ,finances.notes
         );
end