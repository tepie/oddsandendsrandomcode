//
//  zoneclockViewController.m
//  zoneclock
//
//  Created by terrence pietrondi on 11/17/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "zoneclockViewController.h"

@implementation zoneclockViewController
@synthesize estTextField;
@synthesize cstLabel;
@synthesize pstLabel;


/*
// The designated initializer. Override to perform setup that is required before the view is loaded.
- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil {
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}
*/

/*
// Implement loadView to create a view hierarchy programmatically, without using a nib.
- (void)loadView {
}
*/


/*
// Implement viewDidLoad to do additional setup after loading the view, typically from a nib.
- (void)viewDidLoad {
    [super viewDidLoad];
}
*/


// Override to allow orientations other than the default portrait orientation.
- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation {
    return YES;
}

- (void)didReceiveMemoryWarning {
	// Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
	
	// Release any cached data, images, etc that aren't in use.
}

- (void)viewDidUnload {
	// Release any retained subviews of the main view.
	// e.g. self.myOutlet = nil;
}


- (void)dealloc {
	[estTextField release];
	[cstLabel release];
	[pstLabel release];
    [super dealloc];
}

- (IBAction) showTime{
	NSDateFormatter *nsdf = [[NSDateFormatter alloc] init];
	NSLocale *enUSPOSIXLocale;
	enUSPOSIXLocale = [[[NSLocale alloc] initWithLocaleIdentifier:@"en_US_POSIX"] autorelease];
	
	[nsdf setDateFormat:@"hh:mm a"];
	[nsdf setDateStyle:NSDateFormatterNoStyle];
	[nsdf setTimeStyle:NSDateFormatterShortStyle];
	[nsdf setLocale:enUSPOSIXLocale];
	[nsdf setTimeZone:[NSTimeZone timeZoneForSecondsFromGMT:0]];
	
	
	NSLog(@"est text field: %@", self.estTextField.text);	
	
	NSDate *estDate = [nsdf dateFromString:self.estTextField.text];
	NSLog(@"est date obj: %@", estDate);	
	
	[nsdf setDateFormat:@"hh:mm a zzz"];
	[nsdf setTimeZone:[NSTimeZone timeZoneWithAbbreviation:@"CST"]];
	
	self.cstLabel.text = [nsdf stringFromDate:estDate];
	NSLog(@"cst label text: %@", self.cstLabel.text);
	
	[nsdf setTimeZone:[NSTimeZone timeZoneWithAbbreviation:@"PST"]];
	self.pstLabel.text = [nsdf stringFromDate:estDate];
	[nsdf release];
}

@end
