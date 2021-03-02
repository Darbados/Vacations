# Vacations

The Vacations system is mented to be a simple system for tracking employees vacations.
Vacations could vary by type.
Vacations must be approved or rejected, so employee should receive an appropriate 
communication based on the status.
Employee can be hired, he can left, or got fired. Based on that we want to track the period they've been in company.
Based on the hired moment, remaining year vacation should be calculated per specific coef (this vary for countries).
When an year has ended, vacation must be recalculated for the new year. Unused vacation must be tracked as well, and
employee must be notified with its expiration.
Employee should be able to use the system for uploading documents for illness vacation or for civil vacations.
The system can made to allow employee to upload funny materials from holiday vacation, with option which collegues 
of him to be able to see these materials.

We should have roles for:
- approve
- rejection

Vacation could allow employee to show a member of the team which will replace him for the vacation period.
When vacation request is sent, a document for HR could be auto generated and sent to them.

Vacations system should be designed to allow merging vacations data from different sources (API, File imports, etc.).


TODO: 
- Check django docs for static files manage
- Check django docs for templates manage
