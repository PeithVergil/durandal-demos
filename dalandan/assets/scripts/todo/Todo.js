define([
    'knockout'
], function(ko) {
    function Todo(id, title, status) {
        // The primary key.
        this.id = id;

        // The main todo title.
        this.title = ko.observable(title);

        // Temporary storage as 
        // the title is being edited.
        this.draft = ko.observable(title);

        // Has the todo been completed?
        var done = false;

        switch (status) {
            case 2: done = true; break;
        }

        this.done = ko.observable(done);

        // Is the todo beeing updated?
        this.edit = ko.observable(false);
    }

    return Todo;
});