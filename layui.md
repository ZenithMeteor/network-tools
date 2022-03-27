```
{ field: 'oddNumbers', width: 180, title: '单号', sort: true, fixed: 'left', templet: addLink },

function addLink(d) {
　　var addLink = d.oddNumbers;
   if ('' == addLink || null == addLink || undefined == addLink) {
        return '';
   }
   if (addLink.length > 0) {                  
        return '<a class="layui-table-link" href="javascript:void(0);" lay-event="link">' + d.oddNumbers + '</a>';                  
   }
}
```
