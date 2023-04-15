const tag_box = document.querySelector('#tag_box');
const tags_ = document.querySelector('.tags');
let tags = [];
function addTag(id,name)
{
    if(tags.includes(id))
    {
        return
    }
    tags.push(id);
    tag_box.innerHTML += `<p onClick="removeTag(${id})" class="card-btns my" id="tag_${id}">${name}</p>`;

}
function removeTag(id)
{
    var tbox = document.querySelector('#tag_box');
    tags = tags.filter(item => item !== id);
    tbox.querySelector(`#tag_${id}`).remove();
}
