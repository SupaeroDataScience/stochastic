
all:
	mkdocs build
	cd reveal; reveal-md . \
        --template static/template/reveal.html \
        --listing-template static/template/listing.html \
        --css static/css/evo.css \
        --css static/css/reset.css \
        --static-dirs static \
        --static ../../slides

deploy:
	git checkout master
	mkdocs gh-deploy

clean:
	rm -rf site
	rm -rf ../slides
