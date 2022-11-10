const chooseFile = document.getElementById("choose-file");
const imgPreview = document.getElementById("img-preview");

chooseFile.addEventListener("change", function () 
{
  getImgData();
});

function getImgData()
{
  const files = chooseFile.files[0];
  if (files) 
  {
    //document.getElementById("demo").innerHTML = "Hello World";
    const fileReader = new FileReader();
    fileReader.readAsDataURL(files);
    fileReader.addEventListener("load", function () 
    {
      imgPreview.style.display = "block";
      imgPreview.innerHTML = '<img src="' + this.result + '" />';
    });    
  }
}



// function readURL(input) {
//   if (input.files && input.files[0]) {
//       var reader = new FileReader();

//       reader.onload = function (e) {
//           $('#blah')
//               .attr('src', e.target.result)
//               .width(500)
//               .height(500);
//       };

//       reader.readAsDataURL(input.files[0]);
//   }
// }