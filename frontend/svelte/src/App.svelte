<script>
	let  avatar, fileinput, faceName;
	faceName = "svelte";
	
	const onFileSelected = (e) => {
    	let image = e.target.files[0];
		let reader = new FileReader();
		reader.readAsDataURL(image);
		reader.onload = e => {
				avatar = e.target.result
		};
    }
	
	function getFaceName() {
		fetch("http://127.0.0.1:5000/")
			.then(response => {
				console.log(response);
				return response.text();
			})
			.then(data => {
				console.log(data);
				faceName = data;
			})
			.catch(error => console.error('Error:', error));
	}

	$: {
		if (avatar) {
			getFaceName();
		}
	}
</script>

<div id="app">
	<h1>Upload Image</h1>  
        {#if avatar}
        <img class="avatar" src="{avatar}" alt="d" />
        <p>Result: {faceName}</p>
        {:else}
        <img class="avatar" src="https://cdn4.iconfinder.com/data/icons/small-n-flat/24/user-alt-512.png" alt="" /> 
        <p>Result: None</p>
        {/if}

		<img class="upload" src="https://static.thenounproject.com/png/625182-200.png" alt="" on:click={()=>{fileinput.click();}} />

        <input name="face" id="face" style="display:none" type="file" accept=".jpg, .jpeg, .png" on:change={(e)=>onFileSelected(e)} bind:this={fileinput} >

</div>

<style>
	#app{
	display:flex;
		align-items:center;
		justify-content:center;
		flex-flow:column;
}
 
	.upload{
		display:flex;
	height:50px;
		width:50px;
		cursor:pointer;
	}
	.avatar{
		display:flex;
		height:200px;
		width:200px;
	}
</style>

 