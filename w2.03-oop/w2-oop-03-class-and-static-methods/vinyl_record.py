"""
Using the `VinylRecord class`, create a class
attribute that tracks how many records have been
created.

Revise the existing instance method to accommodate
method chaining. We should be able to chain the
`play_record` method like so:

still_bill.play_record().play_record()

Write a reset_total_records class method that
prints a short message to the terminal and resets
the total record count to zero.

Write a get_decade static method to convert a release
year to the corresponding decade.

VinylRecord.get_decade(still_bill.release_year)
# prints "1970"
"""
