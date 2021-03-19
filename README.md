# Servicenow Incident Creation
incident creation in the service now (ITSM tool)

ServiceNow is a cloud-based software platform for IT Service Management (ITSM) which helps to automate IT Business Management. It is designed based on ITIL guidelines to provide service-orientation for tasks, activities, and processes. 

This is the automation using the python language and the jenkins interation where in user can create a P1 (priority1) ticket in the ITSM tool using the jenkins build. 

There are some pre populated field (the ID's) in the script which you can get from the snow API explorer as well or you can use the postman tool for the API reference. 

You need a service account in the servicenow portal which will be used to run this automation on the server side. 

For jenkins pipeline to work, you need to add a snow-node (jenkins slave) and keep the python script over there. The py script should take the string parameter of the jenkins build as the argument and will execute the script.

