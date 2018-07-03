$('#basic').multiselect({
    templates: {
        li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>'
    }
});

$('#no_checkboxes').multiselect({
    templates: {
        li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>'
    },
    nonSelectedText: 'Choose...',
    selectedClass: 'bg-light',
    onInitialized: function(select, container) {
        // hide checkboxes
        container.find('input').addClass('d-none');
    }
});

$('#single_select').multiselect({
    templates: {
        li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>'
    },
    buttonClass: 'btn btn-outline-primary',
    selectedClass: 'bg-light',
    onInitialized: function(select, container) {
        // hide radio
        container.find('input[type=radio]').addClass('d-none');
    }
});

$('#filtering').multiselect({
    nonSelectedText: 'Select a food...',
    enableFiltering: true,
    templates: {
        li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>',
        filter: '<li class="multiselect-item filter"><div class="input-group m-0 mb-1"><input class="form-control multiselect-search" type="text"></div></li>',
        filterClearBtn: '<div class="input-group-append"><button class="btn btn btn-outline-secondary multiselect-clear-filter" type="button"><i class="fa fa-close"></i></button></div>'
    },
    selectedClass: 'bg-light',
    onInitialized: function(select, container) {
        // hide checkboxes
        container.find('input[type=checkbox]').addClass('d-none');
    }
});


// data source example with filter by label
$('#data_source').multiselect({
    templates: {
        li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>'
    },
    nonSelectedText: 'Select a name...',
    enableFiltering: true,
    filterBehavior: 'text',
    enableCaseInsensitiveFiltering: true,
    templates: {
        li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>',
        filter: '<li class="multiselect-item filter"><div class="input-group m-0 mb-1"><input class="form-control multiselect-search" type="text"></div></li>',
        filterClearBtn: '<div class="input-group-append"><button class="btn btn btn-outline-secondary multiselect-clear-filter" type="button"><i class="fa fa-close"></i></button></div>'
    },
});
var options = [
    {label: 'Tony', title: 'Tony', value: '1', selected: true},
    {label: 'Tammy', title: 'Tammy', value: '2'},
    {label: 'Bob', title: 'Bob', value: '3'},
    {label: 'Betty', title: 'Betty', value: '4'},
    {label: 'Jim', title: 'Jim', value: '5', selected: true},
    {label: 'James', title: 'James', value: '6'},
    {label: 'Jerry', title: 'Jerry', value: '7', disabled: true},
    {label: 'Amy', title: 'Amy', value: '8'},
    {label: 'Albert', title: 'Albert', value: '9'}
];
$('#data_source').multiselect('dataprovider', options);

// data source single pick with filter by value and text
var options2 = [
    {label: 'Rex', value: '1'},
    {label: 'Ryan', value: '2'},
    {label: 'Duke', value: '3'},
    {label: 'Kimo', value: '4'},
    {label: 'Vince', value: '5'},
    {label: 'Puggy', value: '6'},
    {label: 'Boxer', value: '7'}
];

$('#data_source_single').multiselect({
    onInitialized: function(select, container) {
        container.multiselect('dataprovider', options2);
        container.multiselect('setOptions', {
            nonSelectedText: 'Select a pooch...',
            enableFiltering: true,
            filterBehavior: 'both',
            enableCaseInsensitiveFiltering: true,
            templates: {
                li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>',
                filter: '<li class="multiselect-item filter"><div class="input-group m-0 mb-1"><input class="form-control multiselect-search" type="text"></div></li>',
                filterClearBtn: '<div class="input-group-append"><button class="btn btn btn-outline-secondary multiselect-clear-filter" type="button"><i class="fa fa-close"></i></button></div>'
            },
            selectedClass: 'bg-light',
        });
        container.multiselect('rebuild');
        $('input[type=radio]').addClass('d-none');
    }
});


